<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-6 offset-3">
        <div id="chat-container" class="card">
          <div class="card-body">
            <div class="container chat-body" ref="chatBody">
              <div v-for="message in messages" :key="message.id" class="row chat-section">
                <template v-if="username === message.sender">
                  <div class="col-sm-7 offset-3">
                    <span class="card-text speech-bubble speech-bubble-user float-right text-white subtle-blue-gradient">
                      {{ message.text }}
                    </span>
                  </div>
                  <div class="col-sm-2">
                    <img class="rounded-circle" :src="`http://placehold.it/40/007bff/fff&text=${message.sender.toUpperCase()}`" />
                  </div>
                </template>
                <template v-else>
                  <div class="col-sm-2">
                    <img class="rounded-circle" :src="`http://placehold.it/40/333333/fff&text=${message.sender.toUpperCase()}`" />
                  </div>
                  <div class="col-sm-7">
                    <span class="card-text speech-bubble speech-bubble-peer">
                      {{ message.text }}
                    </span>
                  </div>
                </template>
              </div>
            </div>
          </div>

          <div class="card-footer text-muted">
            <form @submit.prevent="postMessage">
              <div class="row">
                <div class="col-sm-10">
                  <input v-model="message" type="text" placeholder="Type a message" />
                </div>
                <div class="col-sm-2">
                  <button class="btn btn-primary">Send</button>
                </div>
              </div>
            </form>
          </div>
        </div>


      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      loading: true,
      messages: [],
      message: '',
      ws: new WebSocket(`ws://localhost:8080/chat/${this.$route.params.id}/${sessionStorage.getItem('authToken')}/`)
    }
  },

  created () {
    this.username = sessionStorage.getItem('username');
    if (this.$route.params.id) {
      this.connectToWebSocket();
      this.getMessages();
    }

    // Refresh the JWT every 240 Seconds (4 minutes)
    setInterval(this.refreshToken, 240000)
  },

  updated () {
    // Scroll to bottom of Chat window
    const chatBody = this.$refs.chatBody
    if (chatBody) {
      chatBody.scrollTop = chatBody.scrollHeight
    }
  },

  methods: {
    getMessages(){
      let config = {
        headers: {
          'Authorization': `Token ${sessionStorage.getItem('authToken')}`
         }
        };

      axios.get(`http://localhost:8000/chat/channels/${this.$route.params.id}/messages/`, config)
        .then((resp) => (this.messages = resp.data))
        .catch((err) => (console.log(err)))

    },
    postMessage (event) {
      this.ws.send(''+this.message);
      //this.getMessages()
    },

    fetchChatSessionHistory () {
    },

    connectToWebSocket () {
      console.log(this.$route.params.id);
      this.ws.onopen = this.onOpen;
      this.ws.onclose = this.onClose;
      this.ws.onmessage = this.onMessage;
      this.ws.onerror = this.onError;
      console.log(this.ws.onmessage);
    },

    onOpen(event){
      console.log('Connection opened.', event)
    },

    onClose(event){
      console.log('Connection closed.', event);

      // Try and Reconnect after five seconds
      setTimeout(this.connectToWebSocket, 5000)
    },

    onMessage(event){
      const mes = JSON.parse(event.data);
      if (mes.mtype === 'message'){
        console.log('nt');
        this.messages.push(mes)
      }
      //const message = JSON.parse(event.data);
      //this.messages.push(message);

    },

    onError (event) {
      console.log('!!!', event)
    },

    refreshToken () {
      const data = {token: sessionStorage.getItem('authToken')}

/*      $.post('http://127.0.0.1:8000/this/is/hard/to/find/', data, (response) => {
        sessionStorage.setItem('authToken', response.token)
      })*/
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}

.loading {
  text-align: center;
  margin-top: 150px;
}

.btn {
  border-radius: 0 !important;
}

.card-footer input[type="text"] {
  background-color: #ffffff;
  color: #444444;
  padding: 7px;
  font-size: 13px;
  border: 2px solid #cccccc;
  width: 100%;
  height: 38px;
}

.card-header a {
  text-decoration: underline;
}

.card-body {
  background-color: #ddd;
}

.chat-body {
  margin-top: -15px;
  margin-bottom: -5px;
  height: 380px;
  overflow-y: auto;
}

.speech-bubble {
  display: inline-block;
  position: relative;
  border-radius: 0.4em;
  padding: 10px;
  background-color: #fff;
  font-size: 14px;
}

.subtle-blue-gradient {
  background: linear-gradient(45deg,#004bff, #007bff);
}

.speech-bubble-user:after {
  content: "";
  position: absolute;
  right: 4px;
  top: 10px;
  width: 0;
  height: 0;
  border: 20px solid transparent;
  border-left-color: #007bff;
  border-right: 0;
  border-top: 0;
  margin-top: -10px;
  margin-right: -20px;
}

.speech-bubble-peer:after {
  content: "";
  position: absolute;
  left: 3px;
  top: 10px;
  width: 0;
  height: 0;
  border: 20px solid transparent;
  border-right-color: #ffffff;
  border-top: 0;
  border-left: 0;
  margin-top: -10px;
  margin-left: -20px;
}

.chat-section:first-child {
  margin-top: 10px;
}

.chat-section {
  margin-top: 15px;
}

.send-section {
  margin-bottom: -20px;
  padding-bottom: 10px;
}
</style>

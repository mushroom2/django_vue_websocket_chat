<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-6 offset-3">
        <ul>
          <li v-for="channel in channels" :key="channel.id">
            <a :href="`http://localhost:8000/chat/channels/${channel.id}`" :id="channel.id" @click.prevent = "selectChannel">{{ channel.title}}</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
    import axios from 'axios'
    const token = sessionStorage.getItem('authToken');
    export default {
      data(){
        return {
          channels: [],
          token: ''
        }
      },
    methods: {
      selectChannel(e) {
          this.$router.push('/chat/' + e.target.id)
      }
    },
      created(){

        let config = {
          headers: {
            'Authorization': `Token ${token}`
          }
        };


        axios.get('http://localhost:8000/chat/channels/', config)
          .then( (resp) => this.channels = resp.data)
          .catch( (err) => console.log(err))
      }
    }

</script>

<style scoped>

</style>

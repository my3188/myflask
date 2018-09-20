<template>
  <input type="text" v-model="val">

</template>

<script>
import axios from "axios";

export default {
  name: "tree",
  components: {
    
  },
  data() {
    return {
      val: ""
    };
  },
  methods: {
    onClick() {
      axios
        .get("/api/index")
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  input{
    border: 1px solid red;
  }
</style>

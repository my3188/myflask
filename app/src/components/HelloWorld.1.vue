<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <button @click="onClick">点击我</button>

    <button @click="onAdd">+</button>
    <span class='num' :class='{active:item==activeIndex}'
      @click='onShowInput(item)'
      v-for="(item,index) in TabList"
      :key="index">
      {{item}}
      <button @click.stop="onDel(item)">-</button>
    </span>

    <p>
      <keep-alive>
        <tree></tree>
        <component :is="curComponent"></component>
      </keep-alive>
    </p>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";
import tree from "./tree";
let components = {};
export default {
  name: "main",
  components: {
    tree
  },
  data() {
    return {
      activeIndex:'',
      TabList: [],
      msg: "Welcome to Your Vue.js App"
    };
  },
  computed:{
    curComponent(){
      return "compnt"+this.activeIndex;
    },
  },
  methods: {
    onShowInput(item){
      this.activeIndex = item
      let index = this.list.indexOf(item);
    },
    onAdd() {
      // console.log(this.$options)
      let clone = _.cloneDeep(myinput);
      let i = this.list.length;
      components['compnt'+i] = clone;
      this.list.push(i);
    },
    onDel(item) {
      let index = this.list.indexOf(item);
      this.list.splice(index, 1);
    },
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
a {
  color: #42b983;
}
.num {
  padding: 5px;
  background: #42b983;
  border: 1px solid yellow;
}
.num.active{
  background: #ec7514;
}
</style>

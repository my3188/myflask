<template>
  <div class="hello">

    <button @click="onAdd">+</button>
    <span class='num'
      :class='{active:item.id==activeTab}'
      @click='onShowTree(item)'
      v-for="(item,index) in TabList"
      v-if='!item.isDel'
      :key="index">
      {{item.id}}
      <button @click.stop="onDel(item)">-</button>
    </span>

    <keep-alive>
      <tree v-for="(item,index) in TabList"
        v-if="item.id==activeTab"
        :key='index'></tree>
    </keep-alive>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";
import tree from "./tree";
let components = {};
export default {
  name: "parent-component",
  components: {
    tree
  },
  data() {
    return {
      activeTab: "",
      TabList: []
    };
  },
  computed: {

  },
  methods: {
    onShowTree(item) {
      this.activeTab = item.id;
    },
    onAdd() {
      let id = this.TabList.length;
      let isDel = false;
      this.TabList.push({ id,isDel });
    },
    onDel(item) {
      item.isDel = true;
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
.num.active {
  background: #ec7514;
}
</style>

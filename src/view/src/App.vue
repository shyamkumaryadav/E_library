<template>
  <v-theme-provider root>
    <HelloWorld></HelloWorld>
  </v-theme-provider>
</template>

<script>
import HelloWorld from "./components/HelloWorld";

export default {
  name: "App",

  components: {
    HelloWorld,
  },

  data: () => ({
    name: "Shyamkumar",
  }),
};
</script>

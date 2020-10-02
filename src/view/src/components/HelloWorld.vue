<template>
  <v-card flat>
    <v-toolbar flat height="700">
      <v-switch
        v-model="$vuetify.theme.dark"
        value="$vuetify.theme.dark"
        hint="This toggles the global state of the Vuetify theme"
        inset
        label="Theme light"
        persistent-hint
      ></v-switch>
    </v-toolbar>
  </v-card>
</template>

<script>
// import Vuetify from "vuetify/lib";

export default {
  name: "HelloWorld",
};
</script>

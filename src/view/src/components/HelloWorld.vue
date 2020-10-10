<template>
  <v-container>
    <v-col cols="12" sm="6">
      <v-text-field
        label="Main input"
        :rules="rules"
        outlined
        clearable
        hide-details="auto"
        color="success"
      ></v-text-field>
    </v-col>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      sw: false,
      name: "",
      rules: [
        (value) => !!value || "Required.",
        (value) => (value && value.length >= 3) || "Min 3 characters",
        (value) => value === "shyam" || "shyam",
      ],
    };
  },
};
</script>

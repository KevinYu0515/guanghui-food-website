module.exports = {
  env: {
    browser: true,
    es2021: true
  },
  extends: [
    "plugin:vue/essential",
    "standard"
  ],
  parser: "vue-eslint-parser",
  parserOptions: {
    ecmaVersion: "latest",
    sourceType: "module"
  },
  plugins: [
    "vue"
  ],
  rules: {
    "vue/multi-word-component-names": 0,
    "vue/no-reserved-component-names": 0,
    quotes: [1, "double"]
  }
}

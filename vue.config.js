module.exports = {
  publicPath: process.env.NODE_ENV === "production" ? "/guanghui-food-website/" : "/",

  transpileDependencies: [
    "vuetify"
  ],

  devServer: {
    https: true
  }

}

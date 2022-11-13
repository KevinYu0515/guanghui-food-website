module.exports = {
  publicPath: process.env.NODE_ENV === "production" ? "/guanghui-food-website/" : "/",
  productionSourceMap: false,
  outputDir: "dist",
  assetsDir: "assets",
  devServer: {
    port: 8090,
    host: "0.0.0.0",
    https: true,
    open: true
  }
}

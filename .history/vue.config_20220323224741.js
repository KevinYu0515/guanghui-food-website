

module.exports = {
    publicPath: process.env.NODE_ENV === 'production'?'/光慧水煎包/':'/',

    "transpileDependencies": [
        "vuetify"
        ],

    devServer: {
        https:true
    }
    
}
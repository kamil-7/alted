module.exports = {
  devtool: "source-map",

  entry: {
    style: "./alted/static/sass/main.scss",
    market_detail: "./alted/static/markets/market_detail/index.js",
    coin_detail: "./alted/static/coins/coin_detail/index.js",
    signal_list: "./alted/static/signals/signal_list/index.js",
    signal_detail: "./alted/static/signals/signal_detail/index.js"
  },

  output: {
    filename: "[name].js",
    path: __dirname + "/static/dist",
    publicPath: "http://127.0.0.1:8080/static/dist/"
  },

  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        loader: "babel-loader",
        query: {
          presets: ["react", "es2015", "stage-0", "react-hmre"]
        }
      },
      {
        test: /\.scss$/,
        loader: "style-loader!css-loader!sass-loader"
      },
      { test: /\.css$/, loader: "style-loader!css-loader" }
    ]
  }
};

var webpack = require("webpack");

module.exports = {
  entry: {
    style: "./alted/static/sass/main.scss",
    market_detail: "./alted/static/markets/market_detail/index.js",
    coin_detail: "./alted/static/coins/coin_detail/index.js",
    signal_list: "./alted/static/signals/signal_list/index.js",
    signal_detail: "./alted/static/signals/signal_detail/index.js"
  },

  output: {
    path: __dirname + "/static/dist",
    filename: "[name].js"
  },

  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        loader: "babel-loader",
        query: {
          presets: ["react", "es2015", "stage-0"]
        }
      },
      {
        test: /\.scss$/,
        loader: "style-loader!css-loader!sass-loader"
      },
      { test: /\.css$/, loader: "style-loader!css-loader" }
    ]
  },

  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        NODE_ENV: JSON.stringify("production")
      }
    }),
    new webpack.optimize.UglifyJsPlugin()
  ]
};

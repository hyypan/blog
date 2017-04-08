/**
 * Created by edianzu on 17/4/8.
 */
// webpack.config.js
var path = require('path');
var webpack = require('webpack')
var HtmlWebpackPlugin = require('html-webpack-plugin')



module.exports = {
  entry: [path.join(__dirname, '../src/index')], // file extension after index is optional for .js files
  output: {
    path: path.join(__dirname, '../src/dist/'),
    filename: 'bundle.js'
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin({
      compressor: {
        warnings: false
      }
    }),
    //new webpack.optimize.OccurenceOrderPlugin(),
    new HtmlWebpackPlugin({
      template: './src/index.html'
    })

  ],
  module: {
    loaders: [{
      test: /\.css$/,
      loaders: ['style', 'css']
    }]
  }
};
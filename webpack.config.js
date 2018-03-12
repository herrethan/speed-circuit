const path = require('path');
// const webpack = require('webpack');
// const ExtractTextPlugin = require('extract-text-webpack-plugin');
// const UglifyJsPlugin = require('uglifyjs-webpack-plugin');


module.exports = [];

// bundle sass -> css
module.exports.push({
  entry: './app/static/scss/base.scss',
  output: {
    // This is necessary for webpack to compile but we never use style-bundle.js
    filename: './app/static/dist/style-bundle.js',
  },
  module: {
    rules: [{
      test: /\.scss$/,
      use: [
        {
          loader: 'file-loader',
          options: {
            name: './app/static/dist/style.css',
          },
        },
        { loader: 'extract-loader' },
        { loader: 'css-loader' },
        {
          loader: 'sass-loader',
          options: {
            importer: function(url, prev) {
              if(url.indexOf('@material') === 0) {
                var filePath = url.split('@material')[1];
                var nodeModulePath = `./node_modules/@material/${filePath}`;
                return { file: path.resolve(nodeModulePath) };
              }
              return { file: url };
            }
          }
        }
      ]
    }]
  },
});

// bundle jsx -> js
module.exports.push({
  entry:  __dirname + '/app/static/js/index.jsx',
  output: {
    path: __dirname + '/app/static/dist',
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        // do babel-loader transpiling
        test: /\.jsx$/,
        loader: 'babel-loader',
        options: {
          presets: ['env', 'react']
        }
      },
      {
        // then allow uglification
        test: /\.js$/,
        loader: 'babel-loader',
        enforce: 'pre'
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.jsx']
  }
});

const path = require('path')



module.exports = {
    entry: {
        base: './static/javascript/base.js'
    },
    output: {
        path: path.join(__dirname,'static', 'dist'),
        publicPath: '/',
        filename: '[name].js'
    },
    target: 'web',

    module: {
        rules: [
            {
                // Transpiles ES6-8 into ES5
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
            test: require.resolve('jquery'),
            use: [{
                loader: 'expose-loader',
                options: 'jQuery'
            },{
                loader: 'expose-loader',
                options: '$'
            }]
          }
        ]
    }
}
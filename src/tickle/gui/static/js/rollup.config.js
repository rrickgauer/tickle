/************************************************************************** 

This is the Rollup.JS configuration file.

***************************************************************************/


class RollupConfig
{
    constructor(input, output) {
        this.input = input;

        this.output = {
            format: 'iife',
            compact: true,
            sourcemap: true,
            file: output,
        }
    }
}


const configs = [
    new RollupConfig('custom/pages/new-watch/index.js', 'dist/new-watch.bundle.js'),
];



// rollup.config.js
export default configs;
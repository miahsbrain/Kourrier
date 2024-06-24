/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.{html,js}'],
  theme: {
    extend: {
      fontFamily: {
        'arvo': '"Arvo", serif',
        'space-mono': '"Space Mono", monospace',
        'faustina': '"Faustina", serif',
        'karma': '"Karma", serif',
        'sora': '"Sora", sans-serif',
      }
    },
  },
  plugins: [],
}
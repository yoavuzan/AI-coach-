/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      animation: {
        'pulse-slow': 'pulse-custom 1.5s infinite',
      },
      keyframes: {
        'pulse-custom': {
          '0%': { transform: 'scale(1)', boxShadow: '0 0 0 0 rgba(255, 77, 77, 0.7)' },
          '70%': { transform: 'scale(1.1)', boxShadow: '0 0 0 15px rgba(255, 77, 77, 0)' },
          '100%': { transform: 'scale(1)', boxShadow: '0 0 0 0 rgba(255, 77, 77, 0)' },
        }
      }
    },
  },
  plugins: [],
}

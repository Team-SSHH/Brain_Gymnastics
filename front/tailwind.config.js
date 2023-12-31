/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#96A57B",
        secondary: "#C8CEAA",
        red: "#FF3B3B",
        gray: "#D4D4D4",
      },
      fontFamily: {
        default: ["Pretendard-Regular"],
      },
    },
  },
  plugins: [
    function ({ addUtilities }) {
      const newUtilities = {
        ".no-drag": {
          userSelect: "none",
          "-webkit-user-drag": "none",
          "-khtml-user-drag": "none",
          "-moz-user-drag": "none",
          "-o-user-drag": "none",
          "user-drag": "none",
        },
      };
      addUtilities(newUtilities);
    },
  ],
};

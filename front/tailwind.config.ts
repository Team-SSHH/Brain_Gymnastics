/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#96A57B",
        secondary: "#C8CEAA",
      },
      fontFamily: {
        default: ["Pretendard-Regular"],
      },
    },
  },
  plugins: [
    function ({
      addUtilities,
    }: {
      addUtilities: (utils: { [key: string]: any }) => void;
    }) {
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

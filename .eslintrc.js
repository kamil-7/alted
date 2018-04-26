module.exports = {
  parser: "babel-eslint",
  extends: ["eslint:recommended", "plugin:react/recommended", "prettier"], // extending recommended config and config derived from eslint-config-prettier
  plugins: ["prettier", "react"], // activating esling-plugin-prettier (--fix stuff)

  parserOptions: {
    ecmaVersion: 7,
    sourceType: "module",
    ecmaFeatures: {
      jsx: true
    }
  }
};

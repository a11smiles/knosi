import obsidianPlugin from 'eslint-plugin-obsidianmd';

export default [
  {
    files: ['**/*.ts', '**/*.tsx'],
    plugins: {
      obsidianmd: obsidianPlugin
    },
    rules: {
      ...obsidianPlugin.configs.recommended.rules
    }
  }
];

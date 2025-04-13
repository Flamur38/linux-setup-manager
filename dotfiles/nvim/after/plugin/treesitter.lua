require'nvim-treesitter.configs'.setup {
  ensure_installed = { "python", "json", "yaml", "html", "bash", "javascript" },
  highlight = {
    enable = true,
    additional_vim_regex_highlighting = false,
  },
  indent = { enable = true },
  textobjects = { enable = true }
}



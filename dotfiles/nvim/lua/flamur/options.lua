-- General Neovim Settings

local opt = vim.opt

opt.hlsearch = false
opt.incsearch = true

opt.guicursor = ""

opt.termguicolors = true

-- Disable mouse
opt.mouse = ""  -- ✅ This disables mouse usage completely

-- Line Numbers
opt.relativenumber = true
opt.number = true

-- Tabs & Indentation
opt.tabstop = 4
opt.shiftwidth = 4
opt.softtabstop = 4
opt.expandtab = true
opt.autoindent = true

-- Search Settings
opt.ignorecase = true
opt.smartcase = true

-- Cursor Line
-- opt.cursorline = true

-- Clipboard
opt.clipboard:append("unnamedplus")



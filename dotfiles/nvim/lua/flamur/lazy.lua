local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
	vim.fn.system({
		"git",
		"clone",
		"--filter=blob:none",
		"https://github.com/folke/lazy.nvim.git",
		"--branch=stable",
		lazypath,
	})
end
vim.opt.rtp:prepend(lazypath)

require("lazy").setup({

    -- Comment Plugin (Quickly toggle comments)
    -- Usage:
    --   Comment line:        gcc  (toggle comment on current line)
    --   Comment block:       gbc  (toggle comment on selected block)
    --   Visual mode comment: gc  (select lines and press gc to comment)
    { "numToStr/Comment.nvim", opts = {} },

	-- Python-Specific Enhancements
	{ "mfussenegger/nvim-dap" },               -- Debug Adapter Protocol (DAP)
	{ "mfussenegger/nvim-dap-python" },        -- Python debugging support
	{ "rcarriga/nvim-dap-ui" },                -- UI for debugging
	{ "dense-analysis/ale" },                  -- Linter support (Flake8, Pylint, etc.)

	-- Autocompletion Plugins
	{ "hrsh7th/nvim-cmp" },             -- Completion engine
	{ "hrsh7th/cmp-nvim-lsp" },         -- LSP completion source
	{ "hrsh7th/cmp-buffer" },           -- Buffer words completion
	{ "hrsh7th/cmp-path" },             -- Path autocompletion
	{ "saadparwaiz1/cmp_luasnip" },     -- Snippets completion
	{ "L3MON4D3/LuaSnip" },             -- Snippets engine

	-- Telescope
	{ "nvim-telescope/telescope.nvim", tag = "0.1.8", dependencies = { "nvim-lua/plenary.nvim" } },

	-- Treesitter
	{ "nvim-treesitter/nvim-treesitter", build = ":TSUpdate" },

	-- LSP & Completion
	{
		"VonHeikemen/lsp-zero.nvim",
		branch = "v3.x",
		dependencies = {
			{ "neovim/nvim-lspconfig" },
			{ "williamboman/mason.nvim" },
			{ "williamboman/mason-lspconfig.nvim" },
			{ "hrsh7th/nvim-cmp" },
			{ "hrsh7th/cmp-nvim-lsp" },
			{ "L3MON4D3/LuaSnip" },
		}
	},

    -- { "rose-pine/neovim", name = "rose-pine" },
    -- { "tanvirtin/monokai.nvim", priority = 1000 },
    { "kaiuri/nvim-juliana", lazy = false, priority = 1000, config = true },




	-- Harpoon
	{ "theprimeagen/harpoon" },

})



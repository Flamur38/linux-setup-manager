local lspconfig = require('lspconfig')

-- Ensure Python LSP is installed
require('mason').setup()
require('mason-lspconfig').setup({
	ensure_installed = { "pyright", "lua_ls" }, -- Add "lua_ls" here to ensure it's installed
	automatic_installation = true,
})

lspconfig.pyright.setup({
	on_attach = function(client, bufnr)
		local opts = { buffer = bufnr, remap = false }

		-- LSP Keybindings for Python
		vim.keymap.set("n", "gd", vim.lsp.buf.definition, opts)
		vim.keymap.set("n", "K", vim.lsp.buf.hover, opts)
		vim.keymap.set("n", "<leader>ca", vim.lsp.buf.code_action, opts)
		vim.keymap.set("n", "<leader>rn", vim.lsp.buf.rename, opts)
		vim.keymap.set("n", "[d", vim.diagnostic.goto_prev, opts)
		vim.keymap.set("n", "]d", vim.diagnostic.goto_next, opts)

		-- Auto-format on save with Black
		vim.api.nvim_create_autocmd("BufWritePre", {
			buffer = bufnr,
			callback = function() vim.lsp.buf.format() end
		})
	end,
})

-- ✅ Add this section for Lua LSP to remove "Undefined global `vim`"
lspconfig.lua_ls.setup({
	settings = {
		Lua = {
			diagnostics = {
				globals = { "vim" } -- ✅ Removes the "Undefined global `vim`" warning
			}
		}
	}
})



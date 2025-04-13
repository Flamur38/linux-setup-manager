-- Set leader key
vim.g.mapleader = " "

-- General Remaps
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex) -- Open file explorer

-- Run Python file in a terminal split
vim.keymap.set("n", "<leader>r", ":w<CR>:sp | term python3 %<CR>i", { noremap = true, silent = true })

-- Keep search results centered
vim.keymap.set("n", "n", "nzzzv")
vim.keymap.set("n", "N", "Nzzzv")

-- Replace word under cursor
vim.keymap.set("n", "<leader>s", ":%s/\\<<C-r><C-w>\\>/<C-r><C-w>/gI<Left><Left>")

-- Harpoon Keymaps
local mark = require("harpoon.mark")
local ui = require("harpoon.ui")

vim.keymap.set("n", "<leader>a", mark.add_file)
vim.keymap.set("n", "<C-e>", ui.toggle_quick_menu)
vim.keymap.set("n", "<C-h>", function() ui.nav_file(1) end)
vim.keymap.set("n", "<C-t>", function() ui.nav_file(2) end)
vim.keymap.set("n", "<C-n>", function() ui.nav_file(3) end)
vim.keymap.set("n", "<C-s>", function() ui.nav_file(4) end)

-- Telescope Keymaps
local builtin = require("telescope.builtin")

vim.keymap.set("n", "<leader>pf", builtin.find_files, {})
vim.keymap.set("n", "<C-p>", builtin.git_files, {}) -- Find files in Git
vim.keymap.set("n", "<leader>ps", function()
    builtin.grep_string({ search = vim.fn.input("Grep > ") })
end)

-- Debugging Keymaps (DAP)
local dap = require("dap")

vim.keymap.set("n", "<leader>db", function() dap.toggle_breakpoint() end, { desc = "Toggle Breakpoint" })
vim.keymap.set("n", "<leader>dc", function() dap.continue() end, { desc = "Start Debugging" })
vim.keymap.set("n", "<leader>dn", function() dap.step_over() end, { desc = "Step Over" })
vim.keymap.set("n", "<leader>di", function() dap.step_into() end, { desc = "Step Into" })
vim.keymap.set("n", "<leader>do", function() dap.step_out() end, { desc = "Step Out" })
vim.keymap.set("n", "<leader>dr", function() dap.repl.open() end, { desc = "Open Debug Console" })



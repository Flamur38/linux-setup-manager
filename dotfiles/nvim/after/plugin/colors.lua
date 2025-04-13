function ColorMyPencils(color)
	color = color or "juliana" 
	-- color = color or "rose-pine" 
	vim.cmd("colorscheme " .. color)

    -- Optional: Transparent background (uncomment if desired)
	vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
	vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none" })
end

ColorMyPencils()

-- function ColorMyPencils(color)
-- 	color = color or "juliana" -- or "monokai" etc.
-- 	vim.cmd("colorscheme " .. color)
--
-- 	-- Set solid background color
-- 	vim.api.nvim_set_hl(0, "Normal", { bg = "#303841" })
-- 	vim.api.nvim_set_hl(0, "NormalFloat", { bg = "#303841" })
-- end
--
-- ColorMyPencils()

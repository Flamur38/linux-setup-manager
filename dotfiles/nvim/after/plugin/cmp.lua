local cmp = require("cmp")

cmp.setup({
  snippet = {
    expand = function(args)
      require("luasnip").lsp_expand(args.body) -- Snippet support
    end,
  },
  mapping = cmp.mapping.preset.insert({
    ["<C-p>"] = cmp.mapping.select_prev_item(), -- Previous suggestion
    ["<C-n>"] = cmp.mapping.select_next_item(), -- Next suggestion
    ["<C-y>"] = cmp.mapping.confirm({ select = true }), -- Confirm selection
    ["<C-Space>"] = cmp.mapping.complete(), -- Show completion menu

    -- Tab mapping for selecting suggestions
    ["<Tab>"] = cmp.mapping(function(fallback)
      if cmp.visible() then
        cmp.select_next_item()
      elseif require("luasnip").expand_or_jumpable() then
        require("luasnip").expand_or_jump()
      else
        fallback()
      end
    end, { "i", "s" }),

    ["<S-Tab>"] = cmp.mapping(function(fallback)
      if cmp.visible() then
        cmp.select_prev_item()
      elseif require("luasnip").jumpable(-1) then
        require("luasnip").jump(-1)
      else
        fallback()
      end
    end, { "i", "s" }),
  }),
  sources = cmp.config.sources({
    { name = "nvim_lsp" }, -- LSP-based suggestions
    { name = "buffer" },   -- Words from open buffers
    { name = "path" },     -- File paths
    { name = "luasnip" },  -- Snippets
  }),
})



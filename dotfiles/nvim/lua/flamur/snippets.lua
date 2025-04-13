local ls = require("luasnip") 

ls.add_snippets("python", {
  ls.snippet("def", {
    ls.text_node("def "), ls.insert_node(1, "function_name"), ls.text_node("():"),
    ls.text_node({"", "    "}), ls.insert_node(2, "pass")
  }),
})



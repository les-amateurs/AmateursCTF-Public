# 🕳️	Query the user for input and output the same.
# ❗	Query the user for input and return it.
# ⚠️*string*n1*n2*	Reverse the string from n1 to n2 and return it.
# ❓*string*	Output the string.

# Example:
# ❓*⚠️*❗*1*2** -> [:input, (:reverse, 1, 2), :output]

defmodule Program do
  def tokenize(code) do
    unless code == "" do
      {token, code} = get_token(code)
      [token | tokenize(code)]
    else
      []
    end
  end

  def run(tokens) do
    run(tokens, "")
  end

  def run(tokens, string) do
    unless tokens == [] do
      {token, tokens} = List.pop_at(tokens, 0)

      case token do
        :cat ->
          IO.puts(IO.gets("> "))
          run(tokens, string)

        :input ->
          run(tokens, IO.gets("> ") <> string)

        {:reverse, n1, n2} ->
          string =
            String.slice(string, 0..(n1 - 1)) <>
              String.reverse(String.slice(string, n1..n2)) <>
              String.slice(string, (n2 + 1)..-1//1)

          run(tokens, string)

        :output ->
          IO.puts(string)
          run(tokens, string)

        _ ->
          run(tokens, string <> token)
      end
    else
      string
    end
  end

  defp get_token(code) do
    {token, code} =
      case code |> String.at(0) do
        "🕳️" ->
          {:cat, code |> String.slice(1..-1//1)}

        "❗" ->
          {:input, code |> String.slice(1..-1//1)}

        # start from back and get numbers
        "⚠️" ->
          [n1, n2] =
            code |> String.split("*") |> Enum.slice(-3..-2//1) |> Enum.map(&String.to_integer/1)

          code = code |> String.split("*") |> Enum.slice(1..-4//1) |> Enum.join("*")
          {{:reverse, n1, n2}, code}

        "❓" ->
          {:output, code |> String.slice(2..-2//1)}

        # parse as string literal
        "\"" ->
          token = code |> String.split("\"") |> Enum.at(1)
          {token, ""}

        _ ->
          {nil, code}
      end

    {token, code}
  end

  def main(filename) do
    try do
      code = File.read!(filename)
      code = code |> String.replace("\n", " ") |> String.trim()
      tokens = tokenize(code) |> Enum.reverse()
      #   IO.inspect(tokens)
      run(tokens)
    rescue
      _ in [File.Error, File.Error.ENOENT] ->
        IO.puts("File not found: #{filename}")
        System.halt(1)
    end
  end
end

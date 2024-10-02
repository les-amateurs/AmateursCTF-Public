defmodule Tfsn.FeedFixtures do
  @moduledoc """
  This module defines test helpers for creating
  entities via the `Tfsn.Feed` context.
  """

  @doc """
  Generate a post.
  """
  def post_fixture(attrs \\ %{}) do
    {:ok, post} =
      attrs
      |> Enum.into(%{
        content: "some content"
      })
      |> Tfsn.Feed.create_post()

    post
  end
end

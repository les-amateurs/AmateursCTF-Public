defmodule TfsnWeb.FeedController do
  use TfsnWeb, :controller

  alias Tfsn.Feed
  alias Tfsn.Feed.Post

  action_fallback(TfsnWeb.FallbackController)

  def feed(conn, params \\ %{}) do
    current_user = conn.assigns.current_user
    show_all = params |> Map.has_key?("all")

    posts =
      Feed.list_feed(
        if show_all do
          nil
        else
          current_user
        end
      )

    if current_user != nil do
      render(conn, :feed,
        posts: posts,
        changeset: Post.changeset(%Post{author: current_user.id}, %{})
      )
    else
      render(conn, :feed, posts: posts)
    end
  end

  def post(conn, %{"post" => post_params}) do
    if conn.assigns.current_user.id == 1 do
      conn
      |> put_status(302)
      |> put_flash(:error, "Sorry, admin can't send posts!")
      |> put_resp_header("location", ~p"/")
      |> redirect(to: ~p"/")
    else
      {:ok, _} =
        Feed.create_post(post_params |> Map.put("author_id", conn.assigns.current_user.id))

      conn
      |> put_status(302)
      |> put_flash(:info, "Post successfully sent")
      |> put_resp_header("location", ~p"/")
      |> redirect(to: ~p"/")
    end
  end
end

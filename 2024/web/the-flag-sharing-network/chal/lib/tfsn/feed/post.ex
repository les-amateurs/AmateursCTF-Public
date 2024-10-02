defmodule Tfsn.Feed.Post do
  alias Tfsn.Accounts.User
  use Ecto.Schema
  import Ecto.Changeset

  schema "posts" do
    field :content, :string
    belongs_to :author, User
    # belongs_to :author, User

    timestamps()
  end

  @doc false
  def changeset(post, attrs) do
    post
    |> cast(attrs, [:content, :author_id])
    |> validate_required([:content, :author_id])
  end
end

defmodule Tfsn.Accounts.Follow do
  alias Tfsn.Accounts.User
  use Ecto.Schema
  import Ecto.Changeset

  schema "follows" do
    field :from, :id
    field :to, :id

    timestamps()
  end

  @doc false
  def changeset(follow, attrs) do
    follow
    |> cast(attrs, [])
    |> validate_required([])
  end
end

defmodule Tfsn.Repo do
  use Ecto.Repo,
    otp_app: :tfsn,
    adapter: Ecto.Adapters.Postgres
end

defmodule Tfsn.Repo.Migrations.CreateFollows do
  use Ecto.Migration

  def change do
    create table(:follows) do
      add :from, references(:users), primary_key: true
      add :to, references(:users), primary_key: true

      timestamps()
    end

    create index(:follows, [:from])
    create index(:follows, [:to])
  end
end

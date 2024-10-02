defmodule Tfsn.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  @impl true
  def start(_type, _args) do
    children = [
      # Start the Telemetry supervisor
      TfsnWeb.Telemetry,
      # Start the Ecto repository
      Tfsn.Repo,
      # Start the PubSub system
      {Phoenix.PubSub, name: Tfsn.PubSub},
      # Start Finch
      {Finch, name: Tfsn.Finch},
      # Start the Endpoint (http/https)
      TfsnWeb.Endpoint
      # Start a worker by calling: Tfsn.Worker.start_link(arg)
      # {Tfsn.Worker, arg}
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: Tfsn.Supervisor]
    Supervisor.start_link(children, opts)
  end

  # Tell Phoenix to update the endpoint configuration
  # whenever the application is updated.
  @impl true
  def config_change(changed, _new, removed) do
    TfsnWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end

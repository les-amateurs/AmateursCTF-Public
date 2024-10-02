defmodule TfsnWeb.Router do
  use TfsnWeb, :router

  import TfsnWeb.UserAuth

  pipeline :browser do
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_live_flash
    plug :put_root_layout, {TfsnWeb.Layouts, :root}
    plug :protect_from_forgery
    plug :put_secure_browser_headers
    plug :fetch_current_user
  end

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/", TfsnWeb do
    pipe_through :browser

    get "/", FeedController, :feed
  end

  scope "/", TfsnWeb do
    pipe_through [:browser, :require_authenticated_user]
    post "/post", FeedController, :post
  end

  scope "/@/", TfsnWeb do
    pipe_through :browser

    get "/:username", ProfileController, :feed
    get "/:username/following", ProfileController, :following
    get "/:username/followers", ProfileController, :followers
  end

  scope "/@/", TfsnWeb do
    pipe_through [:browser, :require_authenticated_user]

    get "/:username/follow", ProfileController, :follow
    get "/:username/unfollow", ProfileController, :unfollow
  end

  # Other scopes may use custom stacks.
  # scope "/api", TfsnWeb do
  #   pipe_through :api
  # end

  # Enable LiveDashboard and Swoosh mailbox preview in development
  if Application.compile_env(:tfsn, :dev_routes) do
    # If you want to use the LiveDashboard in production, you should put
    # it behind authentication and allow only admins to access it.
    # If your application does not have an admins-only section yet,
    # you can use Plug.BasicAuth to set up some basic authentication
    # as long as you are also using SSL (which you should anyway).
    import Phoenix.LiveDashboard.Router

    scope "/dev" do
      pipe_through :browser

      live_dashboard "/dashboard", metrics: TfsnWeb.Telemetry
      forward "/mailbox", Plug.Swoosh.MailboxPreview
    end
  end

  ## Authentication routes

  scope "/", TfsnWeb do
    pipe_through [:browser, :redirect_if_user_is_authenticated]

    live_session :redirect_if_user_is_authenticated,
      on_mount: [{TfsnWeb.UserAuth, :redirect_if_user_is_authenticated}] do
      live "/users/register", UserRegistrationLive, :new
      live "/users/log_in", UserLoginLive, :new
    end

    post "/users/log_in", UserSessionController, :create
  end

  scope "/", TfsnWeb do
    pipe_through [:browser]

    delete "/users/log_out", UserSessionController, :delete
  end
end

defmodule TfsnWeb.FollowControllerTest do
  use TfsnWeb.ConnCase

  import Tfsn.AccountsFixtures

  alias Tfsn.Accounts.Follow

  @create_attrs %{

  }
  @update_attrs %{

  }
  @invalid_attrs %{}

  setup %{conn: conn} do
    {:ok, conn: put_req_header(conn, "accept", "application/json")}
  end

  describe "index" do
    test "lists all follows", %{conn: conn} do
      conn = get(conn, ~p"/api/follows")
      assert json_response(conn, 200)["data"] == []
    end
  end

  describe "create follow" do
    test "renders follow when data is valid", %{conn: conn} do
      conn = post(conn, ~p"/api/follows", follow: @create_attrs)
      assert %{"id" => id} = json_response(conn, 201)["data"]

      conn = get(conn, ~p"/api/follows/#{id}")

      assert %{
               "id" => ^id
             } = json_response(conn, 200)["data"]
    end

    test "renders errors when data is invalid", %{conn: conn} do
      conn = post(conn, ~p"/api/follows", follow: @invalid_attrs)
      assert json_response(conn, 422)["errors"] != %{}
    end
  end

  describe "update follow" do
    setup [:create_follow]

    test "renders follow when data is valid", %{conn: conn, follow: %Follow{id: id} = follow} do
      conn = put(conn, ~p"/api/follows/#{follow}", follow: @update_attrs)
      assert %{"id" => ^id} = json_response(conn, 200)["data"]

      conn = get(conn, ~p"/api/follows/#{id}")

      assert %{
               "id" => ^id
             } = json_response(conn, 200)["data"]
    end

    test "renders errors when data is invalid", %{conn: conn, follow: follow} do
      conn = put(conn, ~p"/api/follows/#{follow}", follow: @invalid_attrs)
      assert json_response(conn, 422)["errors"] != %{}
    end
  end

  describe "delete follow" do
    setup [:create_follow]

    test "deletes chosen follow", %{conn: conn, follow: follow} do
      conn = delete(conn, ~p"/api/follows/#{follow}")
      assert response(conn, 204)

      assert_error_sent 404, fn ->
        get(conn, ~p"/api/follows/#{follow}")
      end
    end
  end

  defp create_follow(_) do
    follow = follow_fixture()
    %{follow: follow}
  end
end

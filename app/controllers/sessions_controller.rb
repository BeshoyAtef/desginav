class SessionsController < ApplicationController
 def new
end

def create
  @admin = Admin.authenticate(params[:email], params[:password])
  if @admin
    session[:user_id] = @admin.id
      redirect_to(:controller=>'admin',:action=>'show' ,:id=> @admin.id) 
       flash[:success] = "welcome" 
  else
     flash[:error] = "Invalid email or password"
      render 'new'  
  end
end

def destroy
  session[:admin_id] = nil
  redirect_to root_url, :notice => "Logged out!"
end
end

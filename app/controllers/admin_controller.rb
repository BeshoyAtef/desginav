class AdminController < ApplicationController
	
  def show
  	@admin = Admin.find(params[:id])
   end
   def new 
   	@admin = Admin.new
   end 
end

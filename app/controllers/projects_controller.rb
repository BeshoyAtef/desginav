class ProjectsController < ApplicationController
	def new 
		@project = Project.new
	end 
def create
  @project = Project.new(params[:project])
  @project.save
 
 if  @project.save
   redirect_to(:action => 'show')
else 
	render 'new'
end
end
  def show
  @project = Project.find(params[:id])
end
end

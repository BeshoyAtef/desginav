class Project < ActiveRecord::Base
  attr_accessible :name, :text

  validates :name, presence: true
end

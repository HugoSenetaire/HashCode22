import heapq
from update_function import update_t, update_choose
from write_trajectory import write_trajectory
from get_best_project import get_best_project
from get_best_contributor import get_best_combination
from project_possible_list import is_project_possible, project_possible_list

def roll_project_list_project_possible(contributors, projects, score_function):
  """
  Roll the project list until we fill all projects  
  #Parameters :
  #   contributors : list of <Contributor>
  #   projects : list of <Project>
  #   score_function : function cost that take as input a project, returns a float

  #Return :
  #   trajectory

  """
  nb_project_init = len(projects)
  trajectory = ""
  max_iter = max([project.best_before + project.score for project in projects])
  heap = [0]

  t=0
  while t<max_iter and heap:
      print(f"Iter {t}/{max_iter}")
      if len(projects)<1:
        break

      next_time = heapq.heappop(heap)

      for _ in range(next_time-t +1 ):
        update_t(projects, contributors, t)
        t+=1

      dispo_projects = project_possible_list(projects, contributors)

      while len(dispo_projects)>0:
          print(f"Iter {t}/{max_iter}; Dispo projects {len(dispo_projects)}")
          i,best_project = get_best_project(dispo_projects, score_function) # Return a class Project element
          heapq.heappush(heap,t+best_project.length)
          # TODO: for now we return one possible combination with no cost function, do better
          _,best_contributors = is_project_possible(best_project, contributors)       # 

          projects, contributors = update_choose(projects, contributors, best_project, best_contributors)
          
          trajectory = write_trajectory(trajectory, best_project, best_contributors)
          dispo_projects.pop(i)
          dispo_projects = project_possible_list(dispo_projects, contributors)

  nb_project_final = len(projects)
  trajectory = str(nb_project_init-nb_project_final) +"\n" + trajectory

  return trajectory
        



def roll_project_list_project_contributor_possible(contributors, projects, score_function, max_iter = 1e5):
  """
  Roll the project list until we fill all projects. Difference with previous is we treat contributor and project at the same time for value
  #Parameters :
  #   contributors : list of <Contributor>
  #   projects : list of <Project>
  #   score_function : function cost that take as input a contributor and a project, returns a float

  #Return :
  #   trajectory : Txt file with the trajectory 

  """
  nb_project_init = len(projects)
  trajectory = str("\n")
  t = 0
  while (not len(projects) > 0) and t<max_iter:
      t +=1
      update_t(projects, contributors, t)
      dispo_projects,dispo_contributors = project_contributors_possible_list(projects, contributors)
      while len(dispo_projects)>0 :
          best_project, best_contributor = get_best_project_and_contributors(dispo_projects, contributors, score_function)
          
          update_choose(projects, contributors, best_project, best_contributor)
          trajectory = write_trajectory(trajectory, best_project, best_contributor)

  nb_project_final = len(projects)

  trajectory.insert(0, str(nb_project_init-nb_project_final))

  return trajectory
        

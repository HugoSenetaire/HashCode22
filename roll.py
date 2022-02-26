import heapq
from update_function import update_t, update_choose
from write_trajectory import write_trajectory
from get_best_project import get_best_project
from get_best_contributor import get_best_combination
from project_possible_list import get_projects_bipartite_graph, is_project_possible, remove_impossible_projects_graphs, update_bipartite_graph
from tqdm import tqdm 
from time import time

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
  done_projects_count = 0

  t=0
  while t<max_iter:
      print(f"Iter {t}/{max_iter} - projects done: {done_projects_count}/{nb_project_init}")
      if len(projects)<1:
        break

      # Instead of recomputing all bipartite graphs we only need to recompute rows where the
      # contributor has improved its skills in the last project
      projects_graphs = get_projects_bipartite_graph(projects, contributors)
      remove_impossible_projects_graphs(projects_graphs)
      start = time()
      while len(projects_graphs.columns)>0:
          #TODO: change iter print
          print(f"Iter {t}/{max_iter}; Dispo projects {len(projects_graphs.groupby(level=0, axis=1))}")
          best_project = get_best_project(projects_graphs, score_function) # Return a class Project element
          # print("best_project", time()-start)
          start = time()

          if t+best_project.length not in heap:
            heapq.heappush(heap,t+best_project.length)
          # TODO: for now we return one possible combination with no cost function, do better
          _,best_contributors = is_project_possible(projects_graphs[best_project])       # 

          done_projects_count += 1
          # print("is_project_possible", time()-start)
          start = time()
          projects, contributors = update_choose(projects, contributors, best_project, best_contributors)
          # print("update_chose", time()-start)
          start = time()
          update_bipartite_graph(projects_graphs)
          # print("update_bipartite_graph", time()-start)
          start = time()
          
          trajectory = write_trajectory(trajectory, best_project, best_contributors)
          del projects_graphs[best_project]
          # Contributors have been assigned to a project, update list of possible projects
          # For current time step
          remove_impossible_projects_graphs(projects_graphs)
          # print("remove_impossible_projects_graphs", time()-start)
          start = time()
      
      # No project are in progress
      if not heap:
        break
      # Go to next interestng timestep
      next_time = heapq.heappop(heap)
      for _ in range(next_time-t +1 ):
        update_t(projects, contributors, t)
        t+=1
      


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
        

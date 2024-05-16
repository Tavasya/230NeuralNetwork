from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt


def fig_venn3(venn_type='abc'):

  if venn_type == 'nofig':
    return print('No Diagram')

  #import module
  from matplotlib_venn import venn3, venn3_circles
  from matplotlib import pyplot as plt

  # initialize number of elements by section to scale diagram properly
  An_Bn_C  = 30  # 100/a
  _AnBn_C  = 30  # 010/b
  _An_BnC  = 30  # 001/c
  AnBn_C   = 20  # 110/d
  An_BnC   = 20  # 101/e
  _AnBnC   = 20  # 011/f
  AnBnC    = 10  # 111/g

  # the size_list is for scaling purposes. Do not change the size_list.
  size_list = [An_Bn_C,_AnBn_C,_An_BnC,AnBn_C,An_BnC,_AnBnC,AnBnC]
  venn_set_labels = ['Names','Help','Outside']

  bit_list = ['100','010','001','110','101','011','111']

  if venn_type == 'mult':
    An_Bn_C  = 'Denis,Hayk,\nRay,Lucas,\nMisha,Naomi,\nNyles,\nSteven,Swastik'   # 100/a
    _AnBn_C  = ''   # 010/b
    _An_BnC  = 'Denis,\nHayk,\nSwastik'      # 001/c
    AnBn_C   = ''   # 110/d
    An_BnC   = 'Denis,\nHayk,\nSwastik'     # 101/e
    _AnBnC   = ''      # 011/f
    AnBnC    = ''       # 111/g
    _An_Bn_C = '' # 000/h
    U        = ''      # total number of elements
    venn_labels = [An_Bn_C,_AnBn_C,_An_BnC,AnBn_C,An_BnC,_AnBnC,AnBnC]

  # depict venn diagram
  v = venn3(subsets=(size_list),
            set_labels=(venn_set_labels))

  # set text to defined label id
  v.get_label_by_id(bit_list[0]).set_text(venn_labels[0])
  v.get_label_by_id(bit_list[1]).set_text(venn_labels[1])
  v.get_label_by_id(bit_list[2]).set_text(venn_labels[2])
  v.get_label_by_id(bit_list[3]).set_text(venn_labels[3])
  v.get_label_by_id(bit_list[4]).set_text(venn_labels[4])
  v.get_label_by_id(bit_list[5]).set_text(venn_labels[5])
  v.get_label_by_id(bit_list[6]).set_text(venn_labels[6])

  # set color to defined path id
  v.get_patch_by_id('111').set_color('white')

  # set text to defined label id "A"
  # v.get_label_by_id('A').set_text('A new')

  # add outline
  venn3_circles(subsets=(size_list),
                linestyle="solid",
                linewidth=2)

  #add text at (x, y)
  plt.text(-0.7,0.65, U)        # Universe
  plt.text(0.4,-0.5, _An_Bn_C)  # 000/h

  # Change Backgroud
  plt.gca().set_facecolor('lightgray')
  plt.gca().set_axis_on()

  # assign title
  plt.title('Venn Diagram')

  plt.show()

  return None



fig_venn3("mult")




import pandas as pd

df = pd.read_csv('/CSC 230_ Project - Outside.csv')

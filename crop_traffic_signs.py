# The German Traffic Sign Recognition Benchmark
#
# sample code for reading the traffic sign images and the
# corresponding labels
#
# example:
#            
# trainImages, trainLabels = readTrafficSigns('GTSRB/Training')
# print len(trainLabels), len(trainImages)
# plt.imshow(trainImages[42])
# plt.show()
#
# have fun, Christian

import matplotlib.pyplot as plot
from scipy.misc import imsave #as imsave
import csv
import numpy as np
import random 
# function for reading the images
# arguments: path to the traffic sign data, for example './GTSRB/Training'
# returns: list of images, list of corresponding labels 
def crop_train_traffic_signs(train_path, train_dest, sample_ratio=1.0):
    '''Reads traffic sign data for German Traffic Sign Recognition Benchmark.

    Arguments: path to the traffic sign data, for example './GTSRB/Training'
    Returns:   list of images, list of corresponding labels'''
    images = [] # images
    labels = [] # corresponding labels
    # loop over all 42 classes
    for cls in range(0,43):
        class_path = train_path + '/' + format(cls, '05d') + '/' # subdirectory for class
        meta_data = open(class_path + 'GT-'+ format(cls, '05d') + '.csv') # annotations file
        meta_reader = csv.reader(meta_data, delimiter=';') # csv parser for annotations file
        meta_reader.next() # skip header to the next row:
        # loop over all images in current annotations file
        for row in meta_reader:
            # img -> hog:
            # the 1th column of the row is the filename- contained in the class path:
            img = plot.imread(class_path + row[0])
            cropped_img = img[-int(row[6]):-int(row[4]), int(row[3]):int(row[5])]
            imsave(train_dest +'/'+format(cls,'05d')+'_' + row[0][:-4] + '.png', cropped_img)
            images.append(cropped_img)#.reshape(30,30,3))#.flatten()[:1000])#.tolist()) 
            labels.append(row[7]) # the 8th column of the row is the label"""
        meta_data.close()
    
    # random sampling a portion from training data:
    if sample_ratio == 1.0:
        return images, labels
    train_samples = random.sample(xrange(len(images)), int(sample_ratio*len(images)))
    sample_train_images = np.array(images)[np.array(train_samples)]
    sample_train_labels = np.array(labels)[np.array(train_samples)]
    print "sample train size: ", len(sample_train_images)
    print "first lesson: ", sample_train_images[0].shape
    return sample_train_images, sample_train_labels
def crop_test_traffic_signs(root, test_dest, sample_ratio=1.0):
#plt.imread()
    test_images = [] # images
    test_labels = [] # corresponding labels
    path = root + '/'#path + '/' + format(c, '05d') + '/' # subdirectory for class
    meta = open(path + 'GT-final_test.csv')#+ format(c, '05d') + '.csv') # annotations file
    meta_reader = csv.reader(meta, delimiter=';') # csv parser for annotations file
    meta_reader.next() # skip header
        # loop over all images in current annotations file
    for row in meta_reader:
        # the 1th column is the filename
        img = plot.imread(path + row[0])
        cropped_img = img[-int(row[6]):-int(row[4]), int(row[3]):int(row[5])]
        imsave(test_dest+ '/'+row[7]+'_'+ row[0][:-4]+'.png',cropped_img)
                         
        test_images.append(cropped_img)#.reshape(32,32,3))#.flatten()[:1000])#.reshape(1,))#.tolist()) 
        test_labels.append(row[7]) # the 8th column is the label
    meta.close()
    
    if sample_ratio==1.0:
        return test_images, test_labels
    # random sampling (without replacement) a small set of test images:
    test_samples = random.sample(xrange(len(test_images)), int(sample_ratio*len(test_images)))
#print train_samples
    sample_test_images = np.array(test_images)[np.array(test_samples)]
    sample_test_labels = np.array(test_labels)[np.array(test_samples)]
    print "sample test size: ", len(sample_test_labels)
    print "first test: ", sample_test_images[0].shape
    return sample_test_images, sample_test_labels
    

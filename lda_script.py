import sys
import metapy
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python {} config.toml output_prefix n_topics".format(sys.argv[0]))
        sys.exit(1)
    else:
        _config = sys.argv[1]
        _output_prefix = sys.argv[2]
        _num_topics = int(sys.argv[3])

    metapy.log_to_stderr()

    #Set user specified values
    u_iters = 250
    u_alpha = 0.1
    u_beta = 0.1
    u_k = 15
    u_numdocs = 10 

    fidx = metapy.index.make_forward_index(_config)
    dset = metapy.learn.Dataset(fidx)
    lda_inf = metapy.topics.LDAGibbs(dset, num_topics=_num_topics, alpha=u_alpha, beta=u_beta)
    lda_inf.run(num_iters=u_iters)
    lda_inf.save(_output_prefix)

    model = metapy.topics.TopicModel(_output_prefix)

    with open(_output_prefix+'-topic.txt','w+') as topic:
        for topic_id in range(_num_topics):
            print('Topic ' + str(topic_id))
            print([(fidx.term_text(pr[0]), pr[1]) for pr in model.top_k(tid=topic_id, k = u_k)])
            topic.write('Topic ' + str(topic_id) + '\n')
            for pr in model.top_k(tid=topic_id, k = u_k):
                topic.write(str(fidx.term_text(pr[0])))
                topic.write('\n')
            #topic.write(str([fidx.term_text(pr[0]) for pr in model.top_k(tid=topic_id, k = 20)]))
            topic.write('\n')

    target_doc_count = u_numdocs
    with open(_output_prefix+'-document.txt','w+') as doc:
        
        for d_id in range(target_doc_count):
            print('Document ' + str(d_id))
            print(model.topic_distribution(d_id))
            
            doc.write('Song ' + str(d_id) + '\n')

            doc_scores = []
            is_num = 0
            doc_dist = str(model.topic_distribution(d_id))
            new_doc_str = ''
            for c in doc_dist:
                if(is_num == 1 and c == ' '):
                    continue
                elif(is_num == 1 and (c == ',' or c == '}')):
                    is_num = 0
                    doc_scores.append(new_doc_str)
                    new_doc_str = ''
                elif(is_num == 1 and (c.isdigit() or c == '.')):
                    new_doc_str += c
                if(c == ':'):
                    is_num = 1

            for score in doc_scores:
                doc.write(score)
                doc.write('\n')

            doc.write('\n')



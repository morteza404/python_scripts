import operator

HTTP_OK = 200
HTTP_MULTIPLE_CHOICES = 300
HTTP_BAD_REQUEST = 400
HTTP_CONTINUE = 100

# statuses = [204 for _ in range(4)]

# for hundred in (HTTP_OK, HTTP_MULTIPLE_CHOICES, HTTP_BAD_REQUEST):
#     hstatuses = [(i, s) for i, s in enumerate(statuses) if hundred <= s < hundred + 100]            

# hstatuses = [(i, s) for i, s in enumerate(statuses)]

# print(hstatuses)

indices_to_avoid = set([0,1,2])

# status_index, status = max(((i, stat) for i, stat in hstatuses if i not in indices_to_avoid), key=operator.itemgetter(1))
    
# print(status_index)
# print(status)

def have_quorum(statuses, quorum=None):
        """
        Given a list of statuses from several requests, determine if
        a quorum response can already be decided.

        :param statuses: list of statuses returned
        :param node_count: number of nodes being queried (basically ring count)
        :param quorum: number of statuses required for quorum
        :returns: True or False, depending on if quorum is established
        """
        if quorum is None:
            quorum = 2
        if len(statuses) >= quorum:
            for hundred in (HTTP_CONTINUE, HTTP_OK, HTTP_MULTIPLE_CHOICES,
                            HTTP_BAD_REQUEST):
                if sum(1 for s in statuses
                       if hundred <= s < hundred + 100) >= quorum:
                    return True
        return False

statuses = [404, 404, 404, 404]

# print(have_quorum(statuses))

# for hundred in (HTTP_CONTINUE, HTTP_OK, HTTP_MULTIPLE_CHOICES,HTTP_BAD_REQUEST):
#     total = sum(1 for s in statuses if hundred <= s < hundred + 100)
#     print(total)

def compute_quorum_response():
        if not statuses:
            return None
        for hundred in (HTTP_OK, HTTP_MULTIPLE_CHOICES, HTTP_BAD_REQUEST):
            hstatuses = [(i, s) for i, s in enumerate(statuses) if hundred <= s < hundred + 100]
            if len(hstatuses) >= 2:
                try:
                    status_index, status = max(
                        ((i, stat) for i, stat in hstatuses
                            if i not in indices_to_avoid),
                        key=operator.itemgetter(1))
                except ValueError:
                    # All statuses were indices to avoid
                    continue
                print(status_index)
                print(status)

        #         # resp = status_map[status](request=req)
        #         # resp.status = '%s %s' % (status, reasons[status_index])
        #         # resp.body = bodies[status_index]
        #         # if headers:
        #         #     update_headers(resp, headers[status_index])
        #         # if etag:
        #         #     resp.headers['etag'] = normalize_etag(etag)
        #         # return resp
        # return None
        # return status_index, status

print(compute_quorum_response())
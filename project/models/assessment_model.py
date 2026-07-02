from datetime import datetime
from project.db.connection import connection


OUTCOME_LABELS = {
    "approve": "Approve for Public Access",
    "restrict": "Restrict Access",
    "furtherConsultationRequired": "Further Consultation Required",
}


OUTCOME_TO_ITEM_STATUS = {
    "approve": {"access_level": "Public", "review_status": "Completed"},
    "restrict": {"access_level": "Restricted", "review_status": "Completed"},
    "furtherConsultationRequired": {
        "access_level": "Private",
        "review_status": "Under Review",
    },
}


def get_item(item_id):
    conn = connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM collection_items WHERE item_ID = %s",
        (item_id,)
    )

    item = cur.fetchone()
    cur.close()

    return item


def get_all_items():
    conn = connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT item_ID, title, item_category, cultural_group,
               review_status, access_level
        FROM collection_items
        ORDER BY item_ID
        """
    )

    items = cur.fetchall()
    cur.close()

    return items


def get_reviews(item_id):
    conn = connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT ar.review_ID, ar.review_notes, ar.access_outcome,
               ar.sensitivity_level, ar.conditions_of_use,
               ar.review_timestamp,
               ce.community_name, u.first_name, u.last_name
        FROM access_review ar
        JOIN community_elder ce ON ar.elder_ID = ce.elder_ID
        JOIN user u ON ce.user_ID = u.ID
        WHERE ar.item_ID = %s
        ORDER BY ar.review_timestamp DESC
        """,
        (item_id,)
    )

    reviews = cur.fetchall()
    cur.close()

    return reviews


def get_elders():
    conn = connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT ce.elder_ID, ce.community_name, u.first_name, u.last_name
        FROM community_elder ce
        JOIN user u ON ce.user_ID = u.ID
        ORDER BY u.first_name, u.last_name
        """
    )

    elders = cur.fetchall()
    cur.close()

    return elders


def save_review(
    item_id,
    elder_id,
    review_notes,
    review_outcome,
    sensitivity_level,
    conditions_of_use
):
    conn = connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO access_review (
            item_ID, elder_ID, review_notes, access_outcome,
            sensitivity_level, conditions_of_use, review_timestamp
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            item_id,
            int(elder_id),
            review_notes,
            review_outcome,
            sensitivity_level,
            conditions_of_use,
            datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        )
    )

    status = OUTCOME_TO_ITEM_STATUS[review_outcome]

    cur.execute(
        """
        UPDATE collection_items
        SET access_level = %s,
            review_status = %s
        WHERE item_ID = %s
        """,
        (
            status["access_level"],
            status["review_status"],
            item_id,
        )
    )

    conn.commit()
    cur.close()

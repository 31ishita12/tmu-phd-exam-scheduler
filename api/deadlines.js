// api/deadlines.js

export default function handler(req, res) {
  const { oral } = req.query;
  if (!oral) {
    return res.status(400).json({ error: "Missing query param: ?oral=YYYY-MM-DD" });
  }
  const d = new Date(oral);
  if (isNaN(d)) {
    return res.status(400).json({ error: "Invalid date format, use YYYY-MM-DD" });
  }
  const ms = 24 * 60 * 60 * 1000;
  const written   = new Date(d.getTime() - 14 * ms);
  const schedFrom = new Date(written.getTime() - 21 * ms);
  const schedTo   = new Date(written.getTime() - 14 * ms);
  const proposal  = new Date(d.getTime() - 14 * ms);

  const fmt = dt => dt.toISOString().slice(0, 10);

  res.status(200).json({
    oral_exam:            fmt(d),
    written_exam:         fmt(written),
    sched_request_from:   fmt(schedFrom),
    sched_request_to:     fmt(schedTo),
    proposal_to_committee: fmt(proposal),
  });
}
